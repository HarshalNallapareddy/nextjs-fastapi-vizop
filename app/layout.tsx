// app/layout.tsx

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <title>{'VizOp App'}</title>
        <meta name="description" content={'Visualize stock options with VizOp'} />
      </head>
      <body className={'test'}>
        {children}
      </body>
    </html>
  );
}
