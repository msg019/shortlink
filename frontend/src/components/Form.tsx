import { useState } from "react"
import styles from "./Form.module.css"


export const Form=()=>{
    const [link, setLink]= useState<string>('')
    const [msg,setMsg]= useState<string>('')

    const updateLink=(url:string)=>{
        setLink(url)
    }
    const updateMsg=(message:string)=>{
        setMsg(message)
    }

    const copyLink=()=>{
        navigator.clipboard.writeText(link)

        alert("Link copied to clipboard")
    }

    const HandlerSubmit=(e: React.FormEvent<HTMLFormElement>)=>{
        e.preventDefault()
        const { elements }= e.currentTarget
        const inputs= elements.namedItem('data') as HTMLInputElement

        if(!inputs){return}

        // Clean state
        updateLink('')

        fetch('http://localhost:5000/generate',{
            method: 'POST',
            headers:{
                'Content-type': 'application/json'
            },
            body:JSON.stringify({url: inputs.value})
        })
        .then(res=>
            res.json().then(data=>{
                if (!res.ok){
                    throw new Error(data.error)
                }else{
                    updateLink(data)
                }
            })
        )
        .catch(error=> updateMsg(error.message))

        inputs.value=''

        setTimeout(()=>{
            updateMsg('')
        },5000)
    }
    return(
        <>
            <form onSubmit={HandlerSubmit} className={styles.formContainer}>
                <input 
                    name='data'
                    type='text'
                    required
                />
                <button>Generate</button>
            </form>

            {
                link.length > 1 &&  msg.length==0 &&
                
                <div className={styles.link}>
                    <a href={link} target="_blank">{link}</a>
                    <button onClick={copyLink}>Copy</button>
                </div>
            }
            {
                msg.length > 1 &&
                <div className={styles.error}>
                    <p>{msg}</p>
                </div>
            }
          
        </>
    )
}