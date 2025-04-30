"use client"
import "@/styles/formSection.css"
import Image from 'next/image'
import { useState } from "react";
import { useRouter } from "next/navigation";

//forza únicamente 2 posibles entradas.
type Props = {
    formuse: "create" | "search";
};

export default function FormSection({formuse}: Props){
    //se generan variables de estado con hook useState.
    //question toma la pregunta del usuario.
    //anwer toma la respuesta del usuario.
    //loading habilita o deshabilita la visualización del loader.
    const[question,setQuestion] = useState("");
    const[answer,setAnswer] = useState("");
    const[loading,setLoding] = useState("opacity-0");
    const router = useRouter();
    
    //Función que se ejecuta al enviar form.
    const submitted  = async (e : React.FormEvent<HTMLFormElement>) =>{
        e.preventDefault();
        setLoding("opacity-100");
        

        if(formuse ==="create"){
            try{
                const res = await fetch("http://backend:8000/api/faq",{
                    method:"POST",
                    headers:{"Content-Type": "application/json" },
                    body: JSON.stringify({"question":question,"answer":answer}),
                });
                if (!res.ok) throw new Error("Error en la creación del registro");
                console.log(res)
            } catch(error){
                console.error("Error creando la pregunta", error);
            }
        }
        else if(formuse ==="search"){
            try{
                const res = await fetch("http://localhost:8000/api/search",{
                    method:"POST",
                    headers:{"Content-Type": "application/json" },
                    body: JSON.stringify({"question":question}),
                });
                if (!res.ok) throw new Error("Error en la búsqueda");

                const entry = await res.json()
                const entryId = entry.id;
                router.push(`/faq/${entryId}`);
            } catch(error){
                console.error("Error buscando la pregunta", error);
            }
        }
        //Reinicia variables de estado.
        setQuestion("");
        setAnswer("");
        setLoding("opacity-0");
    }

    //Variables para ajustar diseño del componente dependiendo del uso que se le vaya a dar.
    let title = "";
    let body ="";
    let buttonText ="";
    let bgColor = "";
    let txtColor= "";
    let disp="";
    let id="";
    let loadingDisp ="";
    
    //Asigna valor a las variables anteriores.
    switch(formuse){
        case "create":
            title="Quiero aportar...";
            body ="Para aportar a nuestro repositorio, introduce una pregunta y su respuesta.";
            buttonText ="Enviar";
            bgColor = "bg-(--darkBlue)";
            txtColor="text-white"
            disp="flex";
            id="create";
            loadingDisp="hidden"

            
            break;
        case "search":
            title="Tengo una duda.";
            body ="Si quieres saber algo, ¡pregunta!";
            buttonText ="Buscar";
            bgColor = "bg-white";
            txtColor="text-black";
            disp="hidden";
            id="search";
            loadingDisp="flex";
            
    }
    return(
        <>
        
        <div className={`FormSection-Container ${bgColor}`} id={`${id}`}>

            <span className={`Title-text ${txtColor}`} >{title}</span>
            <span className={`SubTitle-text ${txtColor} mb-2`} >{body}</span>
            
            {/*Inicia cuerpo de Form.*/}
            <form className="form-Container mb-5" onSubmit={submitted}>
                {/*Sección de pregunta.*/}
                <label className={`SubTitle-text ${txtColor} mb-2`} >Mi pregunta...</label>
                <input value={question}  onChange={(e) => setQuestion(e.target.value)} className="Input mb-10 ml-1 rounded-sm placeholder:text-gray-500" type="text" name="question" id="1" placeholder="¿Cuál es la diferencia entre Michael B. Jordan y Michael Jordan?"/>

                {/*Sección de Respuesta.*/}
                <label className={`SubTitle-text ${txtColor} mb-2 ${disp}`} >Mi respuesta...</label>
                <textarea value={answer}  onChange={(e) => setAnswer(e.target.value)} className={`Input mb-10 ml-1 rounded-sm ${disp} placeholder:text-gray-500`}  name="answer" id="2" placeholder="Es un misterio..."/>

                {/*Submit Button.*/}
                <button  className="Input rounded-sm SubTitle-text text-black" type="submit">{buttonText}</button>
            </form>

            {/*Loader condicional.*/}
            <div className={`w-full h-20 align-middle mt-3 ${loadingDisp} justify-center`}>
                <div className={` transition-opacity duration-500 ease-in-out ${loading}`}>
                    <Image src="/bouncing-circles.svg"
                    width={100} height={100} alt="loading svg"/>
                </div>
            </div>

        </div>
        </>
    );
}