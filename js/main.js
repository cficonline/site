function change_bg() {
    // Create an array with all of the image names in it. This is a bit of a hack, but it works for now.
    // TODO: Remove file extensions entirely and just use the number, which would allow me to add images
    const bgs = Array.from(Array(21).keys()).map((i) => `${i + 1}.gif`);
    const random_bg = bgs[Math.floor(Math.random() * bgs.length)];
    const bg_elem = document.querySelector('.bg');
    bg_elem.style.backgroundImage = `url('../img/lain/${random_bg}')`;
}

document.addEventListener('DOMContentLoaded', () => {
    change_bg();
});
