import React from 'react';
import Box from '@mui/material/Box';
import { useTheme } from '@mui/material';

function Footer() {
  const theme = useTheme();

  return (
    <Box
      sx={{
        flexGrow: 1,
        backgroundColor: `${theme.palette.primary.main}`,
        padding: '2rem 2.5rem',
        display: 'flex',
        justifyContent: 'space-between',
      }}
    >
      <div>© 2021 Yonk - Powered by Webflow</div>
      <div>[LOGO]</div>
    </Box>
  );
}

export default Footer;
