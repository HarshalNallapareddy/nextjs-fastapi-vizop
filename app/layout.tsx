// app/layout.tsx
import { Inter } from 'next/font/google';

const inter = Inter({ subsets: ['latin'] });

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <title>{'VizOp App'}</title>
        <meta name="description" content={'Visualize stock options with VizOp'} />
      </head>
      <body className={inter.className}>
        {children}
      </body>
    </html>
  );
}
