
import psi4 
import numpy as np
import matplotlib.pyplot as plt

def order_by_array(x_array, y_array):
    """
    Orders array_y based on x_array
    """
    x_out = np.array(x_array)
    y_out = np.array(y_array)
    indx = x_out.argsort()
    x_out = x_out[indx]
    y_out = y_out[indx]
    
    return x_out, y_out
            
def points_in_z(x_in_blocks, y_in_blocks, z_in_blocks, function, threshold=1e-15):
    
    """
    Finds the ponits of function that are on the z axis.
    
    Parameters
    ----------
    x,y,z: List
        List of numpy arrays with grid blocks
    function: List
        List of block of points of a function
    
    """
    
    x_out = []
    y_out = []

    for block in range(len(x_in_blocks)):                
        x = x_in_blocks[block]
        y = y_in_blocks[block]
        z = z_in_blocks[block]

        for i_point in range(len(x)):
            if np.abs(x[i_point]) < threshold:
                if np.abs(y[i_point]) < threshold:
                    x_out.append(z[i_point])
                    y_out.append(function[block][i_point])

    x_out, y_out = order_by_array(x_out, y_out)
    
    return x_out, y_out

def plot_homo_lumo(wfn):
    """
    Plots HOMO/LUMO alpha/beta orbitals for a molecule ordered on z axis.

    """

    #Orbital Matrices
    Ca = wfn.Ca().clone()
    Cb = wfn.Cb().clone()

    #Create Vpot object
    lda_functional = psi4.driver.proc.dft.lda_functionals.functional_list["svwn"]

    if wfn.same_a_b_orbs() is True:
        functional = psi4.driver.dft.build_superfunctional_from_dictionary(lda_functional, 500000, 1, True)
        functional[0].allocate()
        functional = functional[0]
        Vpot = psi4.core.VBase.build(wfn.basisset(), functional, "RV")
        Vpot.initialize()
        points_func = Vpot.properties()[0]
        points_func.set_pointers(Ca)
    else:
        functional = psi4.driver.dft.build_superfunctional_from_dictionary(lda_functional, 500000, 1, False)
        functional[0].allocate()
        functional = functional[0]
        Vpot = psi4.core.VBase.build(wfn.basisset(), functional, "UV")
        Vpot.initialize()
        points_func = Vpot.properties()[0]
        points_func.set_pointers(Ca, Cb)

    Ca_np = Ca.clone().np
    Cb_np = Cb.clone().np
    nbf = len(Ca_np)

    orbitals_a_r = {str(i_orb) : [] for i_orb in range(nbf)}
    orbitals_b_r = {str(i_orb) : [] for i_orb in range(nbf)}
    x_in_blocks = []
    y_in_blocks = []
    z_in_blocks = []

    for b in range(Vpot.nblocks()):
        block = Vpot.get_block(b)
        points_func.compute_points(block)
        npoints = block.npoints()

        lpos = np.array(block.functions_local_to_global())
        w = np.array(block.w())

        x_in_blocks.append(np.array(block.x()))
        y_in_blocks.append(np.array(block.y()))
        z_in_blocks.append(np.array(block.z()))

        phi = np.array(points_func.basis_values()["PHI"])[:npoints, :lpos.shape[0]]

        #Range specifies number of orbitals requested
        for i_orb in range(2):
            if len(lpos) != 0:
                #C_local = C_np[i_orb, lpos]
                Ca_local = Ca_np[lpos, i_orb]
                Cb_local = Cb_np[lpos, i_orb]
                orb_a = np.einsum('m, pm -> p', Ca_local, phi, optimize=True)
                orb_b = np.einsum('m, pm -> p', Cb_local, phi, optimize=True)
                orbitals_a_r[str(i_orb)].append(orb_a)        
                orbitals_b_r[str(i_orb)].append(orb_b)     

    #Order arrays by z
    x_out, homo_a = points_in_z(x_in_blocks, y_in_blocks, z_in_blocks, orbitals_a_r["0"])
    _,     homo_b = points_in_z(x_in_blocks, y_in_blocks, z_in_blocks, orbitals_b_r["0"])
    _,     lumo_a = points_in_z(x_in_blocks, y_in_blocks, z_in_blocks, orbitals_a_r["1"])
    _,     lumo_b = points_in_z(x_in_blocks, y_in_blocks, z_in_blocks, orbitals_b_r["1"])

    fig, axs = plt.subplots(ncols=2, nrows=2)
    fig.set_figheight(5)
    fig.set_figwidth(10)
    fig.tight_layout()

    p1 = axs[0,0]
    p2 = axs[0,1]
    p3 = axs[1,0]
    p4 = axs[1,1]

    p1.scatter(x_out, homo_a,    c=np.sign(homo_a), cmap="coolwarm", s=3)
    p2.scatter(x_out, homo_b,    c=np.sign(homo_b), cmap="coolwarm", s=3)
    p3.scatter(x_out, lumo_a,    c=-np.sign(lumo_a), cmap="coolwarm", s=3)
    p4.scatter(x_out, lumo_b,    c=-np.sign(lumo_b), cmap="coolwarm", s=3)

    p1.title.set_text("Alpha HOMO")
    p2.title.set_text("Beta HOMO")
    p3.title.set_text("Alpha LUMO")
    p4.title.set_text("Beta LUMO")