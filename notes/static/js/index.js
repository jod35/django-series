const formModal=document.querySelector('.add-modal');
const modalOpenButton=document.querySelector('.add');

modalOpenButton.addEventListener('click',()=>{
    console.log("Hello")
    formModal.style.display="block"
})


const closeModal=(id)=>{
    let el =document.getElementById(id);

    el.style.display="none";
}