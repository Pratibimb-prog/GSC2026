import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Piraksha AI — Piracy Detection & Enforcement",
  description:
    "AI-powered piracy detection system with real-time monitoring, forensic fingerprinting, and automated enforcement.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="h-full antialiased">
      <body className="min-h-full flex flex-col">{children}</body>
    </html>
  );
}
