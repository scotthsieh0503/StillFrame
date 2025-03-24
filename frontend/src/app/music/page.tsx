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
    const [spotifySettings, setSpotifySettings] = useState({
        clientId: '',
        clientSecret: '',
        refreshToken: '',
        accessToken: '',
        mode: 'default',
        blur: 30,
        opacity: 0.5
    });

    useEffect(() => {
        async function getSpotifySettings() {
            try {
                const response = await axios.get(`${STILLFRAME_API_URL}/api/setting/SPOTIFY`);
                const result = response.data.result;
                if (result.CLIENT_ID && result.CLIENT_SECRET) {
                    setSpotifySettings({
                        clientId: result.CLIENT_ID,
                        clientSecret: result.CLIENT_SECRET,
                        refreshToken: result.REFRESH_TOKEN,
                        accessToken: result.ACCESS_TOKEN,
                        mode: result.MODE,
                        blur: result.BLUR,
                        opacity: result.OPACITY
                    });
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
                    'CLIENT_ID': spotifySettings.clientId,
                    'CLIENT_SECRET': spotifySettings.clientSecret,
                    'REFRESH_TOKEN': spotifySettings.refreshToken,
                    'ACCESS_TOKEN': spotifySettings.accessToken,
                    'MODE': spotifySettings.mode,
                    'BLUR': spotifySettings.blur,
                    'OPACITY': spotifySettings.opacity
                });
            } catch (error) {
                console.error('Error saving Spotify settings:', error);
            }
        };

        if (spotifySettings.clientId && spotifySettings.clientSecret) {
            saveSpotifySettings();
        }
    }, [spotifySettings]);

    const handleLogin = () => {
        window.location.href = `${AUTH_ENDPOINT}?client_id=${spotifySettings.clientId}&redirect_uri=${REDIRECT_URI}&response_type=code&scope=${scope}`;
    };

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = e.target;
        setSpotifySettings(prevSettings => ({
            ...prevSettings,
            [name]: value
        }));
    };

    return (
        <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
            <main className="flex flex-col gap-8 row-start-2 items-center items-start">
                <div className='mt-8'>
                    <nav className="breadcrumb">
                        <Link href="/">Home</Link> / <span>Music</span>
                    </nav>
                </div>
                {!spotifySettings.refreshToken && (
                    <div>
                        <label htmlFor="clientId">Spotify Client ID:</label>
                        <input 
                            type="text" 
                            id="clientId" 
                            name="clientId" 
                            value={spotifySettings.clientId}
                            onChange={handleChange}
                            className="border-b p-2 mb-4 w-full"
                        />
                        <label htmlFor="clientSecret">Spotify Client Secret:</label>
                        <input 
                            type="password" 
                            id="clientSecret" 
                            name="clientSecret" 
                            value={spotifySettings.clientSecret}
                            onChange={handleChange}
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
                )}

                {spotifySettings.refreshToken && (
                    <div>
                        <div className="mb-4">
                            <label htmlFor="mode">Album Art Display: </label>
                            <select 
                                id="mode" 
                                name="mode" 
                                defaultValue={spotifySettings.mode}
                                onChange={(e) => setSpotifySettings(prevSettings => ({
                                    ...prevSettings,
                                    mode: e.target.value
                                }))}
                                className="ml-2"
                            >
                                <option value="default">Default</option>
                                <option value="fullscreen">Fullscreen</option>
                            </select>
                        </div>
                        <div className="mb-4">
                            <label htmlFor="blur">Background Blur: </label>
                            <input 
                                type="number" 
                                id="blur" 
                                name="blur" 
                                min="0" 
                                max="100" 
                                step="10"
                                value={spotifySettings.blur}
                                onChange={handleChange}
                                className="ml-2"
                            />
                        </div>
                        <div className="mb-4">
                            <label htmlFor="opacity">Background Opacity: </label>
                            <input 
                                type="number" 
                                id="opacity" 
                                name="opacity" 
                                min="0" 
                                max="1" 
                                step="0.1"
                                value={spotifySettings.opacity}
                                onChange={handleChange}
                                className="ml-2"
                            />
                        </div>                    
                        <div>
                            <h2>Preview: </h2>
                            <img src={`${STILLFRAME_API_URL}/api/music/currently-playing/image/PIL`} alt="Currently Playing" />    
                        </div>
                    </div>
                )}
            </main>
        </div>
    );
}
