'use client'

import React, { useEffect, useState } from 'react';
import axios from 'axios';

const STILLFRAME_API_URL = process.env.NEXT_PUBLIC_API_URL;

interface Track {
    image: string;
    name: string;
    artist: string;
}

export default function CurrenTrack() {
    const [currenTrack, setTrack] = useState<Track | null>(null);

    useEffect(() => {
        async function getCurrentTrack() {
            try {
                const response = await axios.get(`${STILLFRAME_API_URL}/api/music/currently-playing`);
                setTrack(response.data);
            } catch (error) {
                console.error('Error fetching current track:', error);
            }
        };

        getCurrentTrack();
    }, []);

    return (
        <div>
            {currenTrack ? 
                <div className="relative flex justify-center items-center h-screen w-screen bg-white">
                    <div className="absolute inset-0" style={{ background: `url(${currenTrack.image}) center center / cover no-repeat`, filter: 'blur(30px) opacity(0.7)' }}></div>
                    <div className="relative z-10 flex flex-col sm:flex-row items-center sm:items-center bg-whiter">
                        <img src={currenTrack.image} alt="Album cover" width={300} height={300} />
                        <div className="sm:ml-4 mt-4 sm:mt-0 text-center sm:text-left flex flex-col justify-center text-black">
                            <h1 className="text-4xl font-bold">{currenTrack.name}</h1>
                            <h2 className="text-2xl font-bold">{currenTrack.artist}</h2>
                        </div>
                    </div>
                </div>
            : 
            <div className='flex justify-center items-center h-screen w-screen bg-green-500'>
                <img src="/images/spotify.svg" alt="Spotify" style={{ height: '25vh' }} />
            </div>
            }
        </div>
    )
}