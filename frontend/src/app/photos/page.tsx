'use client'

import React, { useEffect, useState } from 'react';
import Heading from '../../components/heading';
import Image from 'next/image';
import axios from 'axios';

export default function PhotosPage() {
    const [selectedFiles, setSelectedFiles] = useState<File[]>([]);
    const [photos, setPhotos] = useState<string[]>([]); // store the uploaded photos
    const [selectedPhotos, setSelectedPhotos] = useState<string[]>([]); // store the uploaded photos
    const STILLFRAME_API_URL = process.env.NEXT_PUBLIC_API_URL;


    // Fetch the uploaded photos
    useEffect(() => {
        axios.get(`${STILLFRAME_API_URL}/api/image/photo`)
            .then((response: any) => {
            setPhotos(response.data.result);
            })
            .catch((error: any) => {
            console.error('Error fetching photos:', error);
            })
    }, [])

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        if (event.target.files) {
            setSelectedFiles(Array.from(event.target.files));
        }
    };

    const handleUpload = () => {
        if (selectedFiles.length > 0) {
            // Handle the file upload logic here
            selectedFiles.forEach(file => {
                const formData = new FormData()
                formData.append('file', file)

                axios.post(`${STILLFRAME_API_URL}/api/image/photo/upload`, formData)
                    .then((response: any) => {
                        //reload the useEffect to fetch the updated photos
                        setPhotos(prevPhotos => [...prevPhotos, response.data.result]);
                        setSelectedFiles([]);
                        
                        console.log('Upload successful:', response.data);
                    })
                    .catch((error: any) => {
                        console.error('Error uploading file:', error);
                    });
            })
        }
    }

    const handleDelete = () => {
        if (selectedPhotos.length > 0) {
            // Handle the file delete logic here
            selectedPhotos.forEach(photo => {
                axios.delete(photo)
                    .then((response: any) => {
                        // Update the photos state by removing the deleted photo
                        setPhotos(prevPhotos => prevPhotos.filter(p => p !== photo));
                        setSelectedPhotos(prevSelected => prevSelected.filter(p => p !== photo));
                        console.log('Delete successful:', response.data);
                    })
                    .catch((error: any) => {
                        console.error('Error deleting photo:', error);
                    });
            });
        }
    }

    const handleSelectPhoto = (photo: string) => {
        setSelectedPhotos(prevSelected => 
            prevSelected.includes(photo) 
                ? prevSelected.filter(p => p !== photo) 
                : [...prevSelected, photo]
        )
    }

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

                {/** Display the uploaded photos */}
                {photos.length > 0 && (
                    <div className='mt-8'>
                        <div>
                            <label>
                                <input 
                                    type="checkbox" 
                                    className='mr-1 mb-4'
                                    onChange={(e) => {
                                        if (e.target.checked) {
                                            setSelectedPhotos(photos);
                                        } else {
                                            setSelectedPhotos([]);
                                        }
                                    }} 
                                    checked={selectedPhotos.length === photos.length && photos.length > 0}
                                />
                                Select All
                            </label>
                            <button className="float-right" onClick={handleDelete}>Delete</button>
                        </div>
                        <div className="grid grid-cols-4 gap-4">
                            {photos.map((photo: string) => (
                                <div 
                                    key={photo} 
                                    className="flex justify-center items-center cursor-pointer" 
                                    onClick={() => handleSelectPhoto(photo)}
                                >
                                    <input 
                                        type="checkbox" 
                                        checked={selectedPhotos.includes(photo)} 
                                        onChange={() => handleSelectPhoto(photo)} 
                                        className="mr-1"
                                    />
                                    <Image 
                                        src={photo} 
                                        width={90}
                                        height={90}
                                        alt="Uploaded photo"
                                        quality={30}
                                        className="w-32 h-32 object-cover rounded-md"
                                        unoptimized
                                    />
                                </div>
                            ))}
                        </div>
                    </div>
                )}
            </main>
        </div>
    );
}