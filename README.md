# Trabajo de Fin de Grado: *Sistema de Información para la toma y gestión de datos en excavaciones arqueológicas*


### Autor(a): Joaquín Alejandro España Sánchez
### Tutor(a)(es): Daniel Sánchez Fernández
___
<p align="center"> 
<a href="https://github.com/alexespana/TFG/actions/workflows/docs.yml"><img src="https://github.com/alexespana/TFG/actions/workflows/docs.yml/badge.svg" alt="Build Docs"></a>
<a href="https://github.com/alexespana/TFG/actions/workflows/build.yml"><img src="https://github.com/alexespana/TFG/actions/workflows/build.yml/badge.svg" alt="Build Images"></a>
<a href="https://github.com/alexespana/TFG/actions/workflows/tests.yml"><img src="https://github.com/alexespana/TFG/actions/workflows/tests.yml/badge.svg" alt="Tests Status"></a>
<a href="https://codecov.io/gh/alexespana/TFG"><img src="https://codecov.io/gh/alexespana/TFG/branch/master/graph/badge.svg?token=IRSGLTKUCT"/></a>
<a href="https://www.gnu.org/licenses/gpl-3.0"><img src="https://img.shields.io/badge/License-GPLv3-blue.svg" alt="License"></a>
</p>

___

La documentación de este proyecto está realizada con `LaTeX`, por lo
tanto para generar el archivo PDF necesitaremos instalar `TeXLive` en
nuestra distribución.

Una vez instalada, tan solo deberemos situarnos en el directorio `doc` y ejecutar:

`
$ pdflatex proyecto.tex
`

Seguido por

    bibtex proyecto
    
y de nuevo

    pdflatex proyecto.tex

O directamente

    make
    
(que habrá que editar si el nombre del archivo del proyecto cambia)

# INSTRUCCIONES

Lee [INSTALL.md](INSTALL.md) para las instrucciones de uso.
