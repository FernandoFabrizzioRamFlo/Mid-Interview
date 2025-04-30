import Header from "@/components/Header";
import HeroBanner from "@/components/Herobanner";
import Introduction from "@/components/Introduction";
import FormSection from "@/components/FormSection";/*
import QaResult from "@/components/QaResult";
*/
export default function Home() {
  return (
    <>
      <main >
        <Header/>
        <HeroBanner/>
        <Introduction/>
        <FormSection formuse="create"/>
        <FormSection formuse="search"/>
        {/*
        <QaResult/>*/}
      </main>
    </>
  );
}
