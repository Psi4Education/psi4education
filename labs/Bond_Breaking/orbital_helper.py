
import psi4 
import numpy as np

def generate_orbitals(wfn, orbitals):
    """
    Generates alpha/beta orbitals on z axis.
    
    Parameters
    ----------
    wfn: psi4.core.Wavefunction
        Wavefunction from calculation
    orbitals: List[int], int>0
        List with requested orbitals
        
    Returns
    -------
    x: np.ndarray
        Numpy array of domain correspoding to z axis.
    orbs_out_a, orbs_out_b: List[np.ndarray]
        List with requested orbitals on z axis. 
    """
    
    if 0 in orbitals:
        raise ValueError("Must provide integer values of orbitals. (i_orb > 0)")

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

    a_orbs = { str(i) : np.empty((1,0)) for i in orbitals  }
    b_orbs = { str(i) : np.empty((1,0)) for i in orbitals  }
    x_out = np.empty((1,0))
    
    for b in range(Vpot.nblocks()):
        block = Vpot.get_block(b)
        points_func.compute_points(block)
        npoints = block.npoints()

        lpos = np.array(block.functions_local_to_global())
        x, y, z = block.x().np, block.y().np, block.z().np
        phi = np.array(points_func.basis_values()["PHI"])[:npoints, :lpos.shape[0]]

        #Range specifies number of orbitals requested
        for i_orb in orbitals:
            if len(lpos) != 0:
                Ca_local = Ca_np[lpos, i_orb-1]
                Cb_local = Cb_np[lpos, i_orb-1]
                orb_a = np.einsum('m, pm -> p', Ca_local, phi, optimize=True)
                orb_b = np.einsum('m, pm -> p', Cb_local, phi, optimize=True)   
                
                #Isolate points close to z axis. 
                mask = np.bitwise_and(np.isclose(x, 0), np.isclose(y, 0))
                if i_orb == orbitals[0]:
                    x_out = np.append(x_out, z[mask])
                a_orbs[ str(i_orb) ] = np.append( a_orbs[str(i_orb)], orb_a[mask] ) 
                b_orbs[ str(i_orb) ] = np.append( b_orbs[str(i_orb)], orb_b[mask] ) 
             
    orbs_out_a = []
    orbs_out_b = []
    #Order points according to z
    indx = np.argsort(x_out)      
    x_out = x_out[indx]
    for i in orbitals:
        orbs_out_a.append( a_orbs[str(i)][indx] )
        orbs_out_b.append( b_orbs[str(i)][indx] )

    
    return x_out, orbs_out_a, orbs_out_b