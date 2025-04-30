import type { Metadata } from "next";
//importar aquí fuentes de google
//import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";



export const metadata: Metadata = {
  title: "Q-Finder - buscador de preguntas y respuestas",
  description: "Encuentra la respuesta a todas tus preguntas. En este sitio se encuentra el repositorio más grande de preguntas y respuestas sobre todos los temas. Si no encuentras algo, puedes aportarlo tú mismo a nuestro repositorio.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        {children}
      </body>
    </html>
  );
}
