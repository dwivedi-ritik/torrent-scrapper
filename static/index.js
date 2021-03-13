
let magnets = document.querySelectorAll(".magnets-inp")
magnets.forEach(mag=>{
    mag.addEventListener('click' , ()=>{
        mag.select()
        document.execCommand('copy')
    })
})