import type { Metadata } from "next";
import { Manrope } from 'next/font/google';
import { Playfair_Display } from "next/font/google";
import "./globals.css";
import "../styles/header.css";

const manrope = Manrope({
  subsets: ["latin"],
  weight: ["200", "300", "400", "500", "600", "700", "800"],
  variable: "--font-manrope",
});
const playfair = Playfair_Display({
  subsets: ["latin"],
  weight: ["400", "700", "900"],
  variable: "--font-playfair",
});

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
      <body className={`${manrope.variable} ${playfair.variable} font-sans`}>
        {children}
      </body>
    </html>
  );
}
