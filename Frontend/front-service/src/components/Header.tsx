import "../styles/header.css"
export default function Header(){
    return(
        <header className="Header-Contaier">
            <div className="Header-Left-Column">
                <span className="Header-Title font-bold">Q-Finder</span>
            </div>
            <div className="Header-Right-Column">
                <a href="#create" className="Header-Button"><span className="Header-Button-Text hover:font-extrabold ">Quiero aportar</span></a>
                <a href="#search" className="Header-Button"><span className="Header-Button-Text hover:font-bold">Tengo una pregunta</span></a>
            </div>
        </header>
    )
}