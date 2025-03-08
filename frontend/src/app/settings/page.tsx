'use client'

import React, { useEffect, useState } from 'react';
import Link from '../../components/link';
import Heading from '../../components/heading';
import axios from 'axios';
import './settings.css'; // Import the CSS file

export default function SettingsPage() {
    const [settings, setSettings] = useState<any>(null);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);
    const STILLFRAME_API_URL = process.env.NEXT_PUBLIC_API_URL;

    useEffect(() => {
        axios.get(`${STILLFRAME_API_URL}/api/setting`)
            .then(response => {
                const data = response.data;
                if (data.message === 'success') {
                    setSettings(data.result);
                } else {
                    setError('Failed to fetch settings');
                }
                setLoading(false);
            })
            .catch(() => {
                setError('Failed to fetch settings');
                setLoading(false);
            });
    }, []);

    const handleSave = (key: string, value: any) => {
        const updatedSettings = { ...settings, [key]: value };
        axios.post(`${STILLFRAME_API_URL}/api/setting/${key}`, value)
            .then(response => {
                const data = response.data;
                if (data.message === 'success') {
                    setSettings(updatedSettings);
                } else {
                    setError('Failed to save settings');
                }
            })
            .catch(() => {
                setError('Failed to save settings');
            });
    };

    return (
        <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
        <main className="flex flex-col gap-8 row-start-2 items-center items-start">
            <div className='mt-8'>
                <nav className="breadcrumb">
                <Link href="/">Home</Link> / <span>Settings</span>
                </nav>
            </div>
            {settings && (
                <div>
                    <div className='mb-8'>
                        <Heading level={2}>Display:</Heading>
                        <div className='ml-5 flex flex-col'>
                            <label>
                                Contrast:
                                <input
                                    className="setting-input"
                                    type="number"
                                    step="0.1"
                                    min="0"
                                    max="1"
                                    value={settings.DISPLAY.CONTRAST}
                                    onChange={(e) => handleSave('DISPLAY', { ...settings.DISPLAY, CONTRAST: parseFloat(e.target.value) })}
                                />
                            </label>
                            <label>
                                Orientation:
                                <select
                                    className="setting-input"
                                    value={settings.DISPLAY.ORIENTATION}
                                    onChange={(e) => handleSave('DISPLAY', { ...settings.DISPLAY, ORIENTATION: e.target.value })}
                                >
                                    <option value="portrait">Portrait</option>
                                    <option value="landscape">Landscape</option>
                                </select>
                            </label>
                            <label>
                                Saturation:
                                <input
                                    className="setting-input"
                                    type="number"
                                    step="0.1"
                                    min="0"
                                    max="1"
                                    value={settings.DISPLAY.SATURATION}
                                    onChange={(e) => handleSave('DISPLAY', { ...settings.DISPLAY, SATURATION: parseFloat(e.target.value) })}
                                />
                            </label>
                        </div>
                    </div>
                    <div className='mb-8'>
                            <Heading level={2}>General:</Heading>
                            <div className='ml-5 flex flex-col'>
                            <label>
                                Mode:
                                <select
                                    className="setting-input"
                                    value={settings.MODE}
                                    onChange={(e) => handleSave('MODE', e.target.value)}
                                >
                                    <option value="Photo">Photo</option>
                                    <option value="Art">Art</option>
                                    <option value="Music">Music</option>
                                </select>
                            </label>
                            <label>
                                Update Interval:
                                <input
                                    className="setting-input"
                                    type="number"
                                    value={settings.UPDATE_INTERVAL}
                                    onChange={(e) => handleSave('UPDATE_INTERVAL', parseInt(e.target.value))}
                                />
                                seconds
                            </label>
                        </div>
                     </div>
                </div>
            )}
        </main>
        </div>
    );
};
