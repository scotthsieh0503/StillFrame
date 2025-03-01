'use client'

import React, { useState } from 'react';
import Heading from '../../components/heading';

export default function PhotosPage() {
    const [selectedFiles, setSelectedFiles] = useState<File[]>([]);

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        if (event.target.files) {
            setSelectedFiles(Array.from(event.target.files));
        }
    };

    const handleUpload = () => {
        if (selectedFiles.length > 0) {
            // Handle the file upload logic here
            selectedFiles.forEach(file => {
                console.log('Uploading file:', file);
            });
        }
    };

    return (
        <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
            <main className="flex flex-col gap-8 row-start-2 items-center sm:items-start">
                <Heading level={1}>Photos</Heading>
                <input 
                    type="file" 
                    accept="image/*" 
                    multiple 
                    onChange={handleFileChange} 
                />
                <button onClick={handleUpload}>Upload</button>
            </main>
        </div>
    );
}