import React, { JSX } from 'react';

type HeadingProps = {
  className?: string;
  level: 1 | 2 | 3 | 4 | 5 | 6;
} & React.HTMLProps<HTMLElement>; // Extend with standard HTML element props for more flexibility



const Heading: React.FC<HeadingProps> = ({ level = 1, className, ...props }) => {
  const Element = `h${level}` as keyof JSX.IntrinsicElements; // Ensures that Element is a valid JSX element type
  return <Element {...props} className={className} />;
};

export default Heading;