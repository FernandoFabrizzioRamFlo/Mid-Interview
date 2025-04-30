
type FAQ = {
    question: string;
    answer: string;
};

export default async function Page({ params }: { params: { id: string } }) {
    const res = await fetch(`http://localhost:8000/api/faq/${params.id}`, {
        cache: "no-store",
    });

    const faq: FAQ = await res.json();

    return (
        <div className="p-8">
            <h1 className="text-xl font-semibold mb-4">{faq.question}</h1>
            <p className="text-gray-800">{faq.answer}</p>
        </div>
    );
}
