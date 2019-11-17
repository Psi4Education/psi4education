Contributing to Psi4Education
=========================

Welcome to the Psi4Education Developer Community! 

The single largest factor which makes this repository an effective resource is
that it was inspired by, designed for, and maintained by university faculty who
teach chemistry -- and who are invested in bringing quantum & computational
chemistry to the wider chemistry curriculum.  Therefore, your contributions to
this project are vital: through reporting issues, contributing to discussions
on posts and pull requests, and/or submitting labs of your own, you can impact
how this project moves forward and how well we serve yours as well as the needs
of the community. 

The following are a set of suggestions for the best way to contribute to the
Psi4Education project. Just like the Code of the Pirate Brethren set forth by
Morgan and Bartholomew, they're more what you'd call "guidelines" than actual
rules.  Hopefully, however, this document (and the guidelines inside) will make
contributing to Psi4Education both easier and more effective for everyone.  

Good luck & happy coding!

-- The Psi4Education Developers 

#### Table of Contents

1. [What do I need to know before starting to contribute to Psi4Education?](#what-do-i-need-to-know-before-starting-to-contribute-to-psi4education)
2. [How can I contribute to Psi4Education?](#how-can-i-contribute-to-psi4education)
    * [Beginner Labs](#beginner-labs)
    * [Advanced Labs](#advanced-labs) 
3. [Styleguides](#styleguides)
    1. [Python Styleguide](#python-styleguide)
    2. [Citation Styleguide](#citation-styleguide)
    3. [Header Styleguide](#header-styleguide)
    4. [Documentation Sytleguide](#documentation-styleguide)
4. [Possible development workflow](#possible-development-workflow)

# What do I need to know before starting to contribute to Psi4Education?

The strategic goals of the Psi4Education project are to provide the chemistry education
community with
* goal1
* goal2
to facilitate incorporating quantum & computational chemistry into the broader chemistry
curriculum.

For more information on these goals, refer to the [reference
implementation](#reference-implementations) and [interactive
tutorial](#interactive-tutorials) sections below, as well as the project
overview [here](https://github.com/psi4/psi4education#overview).  This repository contains

* beginner labs, which provide laboratory exercises for under-division students, and
* advanced labs, which provide laboratory exercises targeted at upper-division students.

# How can I contribute to Psi4Education?

There are several ways to become involved with Psi4Education, including 

* participating in discussions on [pull
requests](https://github.com/psi4/psi4education/pulls) and
[issues](https://github.com/psi4/psi4education/issues),
* updating/adding features to existing content, and
* submitting new content to the repository.

Each of these possible contributions are highly valuable, and will help
Psi4Education to better serve the needs of the chemical education chemistry
community at large. Therefore, your contribution is crucial to the success of
this project!

Below, guidelines for submitting new content are discussed, first for [beginner
labs](#beginner-labs) and then for [advanced labs](#advanced-labs). For
convenience, a possible development workflow is given
[here](#suggested-workflow).

## Beginner Labs

blah blah blah

some description of the goals of the beginner labs

blah blah blah

## Advanced Labs

For more advanced or upper-division students, we have a suite of laboratory
exercises.  

## Styleguides

### Python Styleguide

All Python code should should conform to the
[PEP8](https://www.python.org/dev/peps/pep-0008/) Python style guide
conventions.  This code should be compliant with Python versions 3.5/3.6/3.7/+
meaning that `print` must be called as a function, i.e., `print('Compliant with
Python 3')` and not `print 'This will break Python 3!'`.

### Citation Styleguide

> TL;DR: Citations, including equation numbers, should be provided in close
> proximity (docstrings or comments) to the code. It can also be handy to collect
> all citations into the nearest README.md (for reference implementations) or
> final cell (for tutorials).

For both reference implementations and interactive tutorials, a complete list
of citations from which the content was drawn must be provided.  Such citation
lists should contain entries of the form (in Markdown):
```
1. [LNFA:yy:pp](https://link-to-publication-website.com) J. Doe *et al.* *J. Abbrev.* **Issue**, pages (year)
```
The LNFA:yy:pp citation key contains the last name of the first author (LNFA),
the publication year (yy), and the publication pages (pp), and the full
citation should be supplied in [AIP
format](https://publishing.aip.org/authors/preparing-your-manuscript) (see link
section Refernces -- By Number).  

For reference implementations, citations should appear 

* as full list items in the "References" section of the relevant method
directory's `README.md` file (see [Repository
Organization](#repository-organization) above), and 
* as keys followed by relevant equation information in code comments/function docstrings.  

This final point is important when specific equations from a publication are
implemented within the script.  In this case, a Python comment containing this
publication's citation key and the equation number for the expression
beingimplemented should be given nearby.  For example, to implement a function
which builds the `Wmnij` intermediate from equation 6 of [J. F.  Stanton *et
al.*'s paper](http://dx.doi.org/10.1063/1.460620), 
```python
def build_Wmnij():
    """Implements [Stanton:1991:4334] Eqn. 6"""
    code code code
```

For interactive tutorials, unlike for reference implementations, a references
section within each tutorial should be included in a markdown cell at the very
end of the notebook.  This cell should contain a citation list of the form
above.  Since the tutorials are effectively standalone entities, however, this
`Tutorial References` section should *not* be augmented with a central
references section within the method's README.  Additionally, specific
equations should be referenced within tutorials using the citation key for the
appropriate publication.

### Header Styleguide

Each reference implementation script and tutorial notebook should begin with a
statement about the purpose of the script, author and contributor information,
and copyright, license, and date information (in [YYYY-MM-DD format](https://en.wikipedia.org/wiki/ISO_8601)):

```python
"""
A simple explanation of script contents.

References:
Algorithms taken from: https://some-source-url.com
Equations taken from: [LNFA:yy:pp] and [LNFA:yy:pp]
"""

__authors__   =  "John and Jane Doe"
__credits__   =  ["John Doe", "Jane Doe", "John Q. Sample"]

__copyright__ = "(c) 2014-2018, The Psi4Education Developers"
__license__   = "BSD-3-Clause"
__date__      = "2017-05-23"
```

The difference between `__authors__` and `__credits__` is largely semantic;
one possible delineation can be summarized by

* `__author__`: individuals who have written/modified large parts of the script/code
* `__credits__` : individuals who cleaned up or modified the code slightly.

In this way, all contributions are recognized and retained, no matter the scope.

### Documentation Styleguide

Documentation for the contents of the Psi4Education repository is contained in
`README.md` files in each directory.  

For reference implementations, `README.md` files in the `method-dir` should contain
* a *very* brief overview of the most important aspects of the theory,
* a description of the primary arrays, variables, and indices for the method,
* a description of the proper use and capabilities of any helper classes or modules, and
* a list containing relevant citations for all scripts in the `method-dir` (see [above](#citation-styleguide))
See the SAPT README [here](https://github.com/psi4/psi4education/blob/master/Symmetry-Adapted-Perturbation-Theory/README.md)
for an example.

For interactive tutorials, two levels of `README.md` files exist.  First, the
`README` for the main `Tutorials` folder
[here](https://github.com/psi4/psi4education/tree/master/Tutorials) contains a list
of available tutorials grouped by module.  Second, in each
`module-dir/README.md`, a more detailed list of the module and individual
tutorial contents is given.  See the Hartree--Fock module README
[here](https://github.com/psi4/psi4education/blob/master/Tutorials/03_Hartree-Fock/README.md)
for an example.

## Development Workflow

The Psi4Education repository has adopted the forking workflow within Github: the
[what](https://www.atlassian.com/git/tutorials/comparing-workflows#forking-workflow)
and
[how](http://psicode.org/psi4manual/1.1/build_obtaining.html#what-is-the-suggested-github-workflow)
(replace `psi4.git` with `psi4education.git`) of this process has been discussed elsewhere.  Additionally, the [GitHub
guide](https://guides.github.com/introduction/flow/) provides a graphical
representation which visualizes this process.

