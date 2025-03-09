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
        <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
        <main className="flex flex-col gap-8 row-start-2 items-center items-start">
                    <div className='mt-8'>
                        <nav className="breadcrumb">
                        <Link href="/">Home</Link> / <span>{pageHeader}</span>
                        </nav>
                    </div>
                    <ImageUploader folder={slug} />
                </main>
        </div>
    )
}