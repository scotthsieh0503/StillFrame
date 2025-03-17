"use client"

import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import Image from 'next/image';
import axios from 'axios';

const STILLFRAME_CLIENT_URL = process.env.NEXT_PUBLIC_CLIENT_URL || '';
const STILLFRAME_API_URL = process.env.NEXT_PUBLIC_API_URL || '';
const REDIRECT_URI = `${STILLFRAME_CLIENT_URL}/music/callback`;


const AUTH_ENDPOINT = 'https://accounts.spotify.com/authorize';
const scope = 'user-read-private user-read-email user-read-playback-state user-modify-playback-state user-read-currently-playing';

export default function MusicPage() {
    const [clientId, setClientId] = useState('');
    const [clientSecret, setClientSecret] = useState('');
    const [refreshToken, setRefreshToken] = useState('');
    const [accessToken, setAccessToken] = useState('');

    useEffect(() => {
        async function getSpotifySettings() {
            try {
                const response = await axios.get(`${STILLFRAME_API_URL}/api/setting/SPOTIFY`);
                const result = response.data.result;
                if (result.CLIENT_ID && result.CLIENT_SECRET) {
                    setClientId(result.CLIENT_ID)
                    setClientSecret(result.CLIENT_SECRET)
                    setRefreshToken(result.REFRESH_TOKEN)
                    setAccessToken(result.ACCESS_TOKEN)
                }
            } catch (error) {
                console.error('Error fetching Spotify settings:', error);
            }
        };

        getSpotifySettings();
    }, []);

    useEffect(() => {
        const saveSpotifySettings = async () => {
            try {
                await axios.post(`${STILLFRAME_API_URL}/api/setting/SPOTIFY`, {
                    'CLIENT_ID': clientId,
                    'CLIENT_SECRET': clientSecret,
                    'REFRESH_TOKEN': refreshToken,
                    'ACCESS_TOKEN': accessToken
                });
            } catch (error) {
                console.error('Error saving Spotify settings:', error);
            }
        };

        if (clientId && clientSecret) {
            saveSpotifySettings();
        }
    }, [accessToken, clientId, clientSecret, refreshToken]);

    const handleLogin = () => {
        window.location.href = `${AUTH_ENDPOINT}?client_id=${clientId}&redirect_uri=${REDIRECT_URI}&response_type=code&scope=${scope}`;
    };

    return (
        <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
            <main className="flex flex-col gap-8 row-start-2 items-center items-start">
                <div className='mt-8'>
                    <nav className="breadcrumb">
                        <Link href="/">Home</Link> / <span>Music</span>
                    </nav>
                </div>
                <div>
                    <label htmlFor="clientId">Spotify Client ID:</label>
                    <input 
                        type="text" 
                        id="clientId" 
                        name="clientId" 
                        value={clientId}
                        onChange={(e) => setClientId(e.target.value)}
                        className="border-b p-2 mb-4 w-full"
                    />
                    <label htmlFor="clientSecret">Spotify Client Secret:</label>
                    <input 
                        type="password" 
                        id="clientSecret" 
                        name="clientSecret" 
                        value={clientSecret}
                        onChange={(e) => setClientSecret(e.target.value)}
                        placeholder='********'
                        className="border-b p-2 mb-4 w-full"
                    />
                    <button 
                        onClick={handleLogin} 
                        className="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-full flex items-center"
                    >
                        <Image 
                            src="/images/spotify.svg"
                            alt="Spotify" 
                            width={24}
                            height={24}
                            className="mr-2"
                        />
                        Connect to Spotify
                    </button>
                </div>
            </main>
        </div>
    );
}
