type FAQ = {
    question: string;
    answer: string;
};

interface PageProps {
    params: {
        id: string;
    };
}
export default async function Page({ params }: PageProps) {
    const res = await fetch(`http://backend:8000/api/faq/${params.id}`, {
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
