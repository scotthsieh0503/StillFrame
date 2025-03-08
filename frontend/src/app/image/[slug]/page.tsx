import React from 'react';
import ImageUploader from './imageUplaoder'
import Link from '../../../components/link';

export const generateStaticParams = async () => {
    const slugs = ['photo', 'art', 'sketch'];
    return slugs.map((slug) => ({ slug }));
  };

export default function ImagePage({ params }: { params: { slug: string } }) {
    const { slug } = params;
    const pageHeader = slug.charAt(0).toUpperCase() + slug.slice(1);
    return (
        <main className="mx-auto w-full max-w-4xl px-4 py-8 grid gap-8 items-start">
            <div className='mt-8'>
                <nav className="breadcrumb">
                <Link href="/">Home</Link> / <span>{pageHeader}</span>
                </nav>
            </div>
            <ImageUploader folder={slug} />
        </main>
    )
}