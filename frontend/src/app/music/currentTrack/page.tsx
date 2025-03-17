'use client'

import React, { useEffect, useState } from 'react';
import Image from 'next/image';
import axios from 'axios';

const STILLFRAME_API_URL = process.env.NEXT_PUBLIC_API_URL;
const SPOTIFY_API_URL = 'https://api.spotify.com';

export default function CurrenTrack() {
    const [albumArt, setAlbumArt] = useState('');
    const [currentTrack, setCurrentTrack] = useState('');

    useEffect(() => {
        const fetchNowPlaying = async () => {
            try {
                const tokenResponse = await axios.get(`${STILLFRAME_API_URL}/api/setting/SPOTIFY`);
                const accessToken = tokenResponse.data.result.ACCESS_TOKEN;
                const response = await axios.get(`${SPOTIFY_API_URL}/v1/me/player/currently-playing`, {
                    headers: {
                        Authorization: `Bearer ${accessToken}`
                    }
                });
                console.log('response', response);
                const data = response.data;
                setCurrentTrack(data);
                if (data && data.item && data.item.album && data.item.album.images) {
                    setAlbumArt(data.item.album.images[0].url);
                }
            } catch (error) {
                console.error('Error fetching now playing track:', error);
            }
        };

        fetchNowPlaying();
    }, []);

    return (
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
             <Image src="/images/spotify.svg" alt="Spotify" width={24} height={24}/>
        </div>
    )
}