import Link from '../components/link';


export default function Home() {
  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-8 row-start-2 items-center sm:items-start">
        <div>
          <Link href="/image/photo">Photo</Link>
        </div>
        <div>
          <Link href="/image/art">Art</Link>
        </div>
        <div>
          <Link href="/music">Music</Link>
        </div>
        <div>
          <Link href="/settings">Settings</Link>
        </div>
      </main>
    </div>
  );
}
