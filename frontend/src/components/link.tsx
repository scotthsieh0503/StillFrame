import React from 'react';
import NextLink from 'next/link';

interface LinkProps {
  href: string;
  children?: React.ReactNode;
  className?: string;
}

const Link: React.FC<LinkProps> = ({ href, className, children, ...props }) => (
  <NextLink href={href} className={className} {...props} passHref>{children}</NextLink>
);

export default Link;