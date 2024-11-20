// Capturamos la imagen
const heroImage = document.querySelector('.hero img');


// Crear un método que reciba el número de la imagen y modifique el valor del src
const changeImage = (pNumImage) => heroImage.src = `/static/images/imagen${pNumImage}.png`;

// setInterval para que cada cierto tiempo cambie la imagen
let numeroImagen = 1;
const intervalo = setInterval(() => {
    numeroImagen = (numeroImagen < 3) ? numeroImagen + 1 : 1;
    changeImage(numeroImagen);

}, 3000)

const pararCarrusel = () => {
    clearInterval(intervalo);
}