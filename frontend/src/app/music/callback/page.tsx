"use client"

import React, { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import axios from 'axios';

const STILLFRAME_CLIENT_URL = process.env.NEXT_PUBLIC_CLIENT_URL;
const STILLFRAME_API_URL = process.env.NEXT_PUBLIC_API_URL;
const REDIRECT_URI = `${STILLFRAME_CLIENT_URL}/music/callback`;

export default function MusicPage() {
    const router = useRouter();
    const [clientId, setClientId] = useState('');
    const [clientSecret, setClientSecret] = useState('')
    const [authenticated, setAuthenticated] = useState(false);
    const TOKEN_ENDPOINT = 'https://accounts.spotify.com/api/token';

    useEffect(() => {
        async function getSpotifySettings() {
            try {
                const response = await axios.get(`${STILLFRAME_API_URL}/api/setting/SPOTIFY`);
                const result = response.data.result;
                if (result.CLIENT_ID && result.CLIENT_SECRET) {
                    setClientId(result.CLIENT_ID)
                    setClientSecret(result.CLIENT_SECRET)
                }
            } catch (error) {
                console.error('Error fetching Spotify settings:', error);
            }
        };

        getSpotifySettings();
    }, []);

    useEffect(() => {
        const handleCallback = async () => {
            const urlParams = new URLSearchParams(window.location.search);
            const code = urlParams.get('code');

            if (code && clientId && clientSecret) {
                const response = await axios.post(TOKEN_ENDPOINT, new URLSearchParams({
                    grant_type: 'authorization_code',
                    code: code,
                    redirect_uri: REDIRECT_URI
                }), {
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Authorization': 'Basic ' + btoa(`${clientId}:${clientSecret}`)
                    }
                });

                const data = response.data;
                const { access_token, refresh_token } = data;
                try {
                    await axios.post(`${STILLFRAME_API_URL}/api/setting/SPOTIFY`, {
                        ACCESS_TOKEN: access_token,
                        REFRESH_TOKEN: refresh_token,
                        CLIENT_ID: clientId,
                        CLIENT_SECRET: clientSecret
                    });
                } catch (error) {
                    console.error('Error saving Spotify tokens:', error);
                }

                // Redirect to another page or handle the authenticated state
                // Set state marking authentication as success
                setAuthenticated(true)
            }
        };

        handleCallback();
    }, [router, clientId, clientSecret]);

    return (
        <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
            <main className="flex flex-col gap-8 row-start-2 items-center items-start">
                <div className='mt-8'>
                    <nav className="breadcrumb">
                        <Link href="/">Home</Link> / <span>Music</span>
                    </nav>
                </div>
                {authenticated && (
                    <div className="flex items-center gap-2 text-green-600">
                        <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                            <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                        </svg>
                        <span>Authenticated successfully</span>
                    </div>
                )}
            </main>
        </div>
    )
}