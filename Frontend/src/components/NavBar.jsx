import React from 'react';
import { NavLink } from 'react-router-dom';
import { useTheme, AppBar, Box, Toolbar, Button } from '@mui/material';

const menuItems = [
  {
    label: 'Home',
    href: '/',
  },
  {
    label: 'About',
    href: '/about',
  },
  {
    label: 'Contact',
    href: '/contact',
  },
];

function NavBar() {
  const theme = useTheme();

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar
        elevation={0}
        position="fixed"
        sx={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          backgroundColor: 'transparent',
          padding: '2rem 2.5rem',
        }}
      >
        <Toolbar
          disableGutters
          sx={{
            width: '100%',
            display: 'flex',
            justifyContent: 'space-between',
          }}
        >
          <NavLink to="/">
            <img
              src="https://assets.website-files.com/60ec04708eb66b625fc4fb1e/6117c1783980cfef5fb1fa31_yonk.logo.svg"
              loading="lazy"
              alt=""
              class="logo"
              style={{ width: '12.5rem' }}
            />
          </NavLink>
          <Box
            sx={{
              padding: '0 1.25rem',
              borderStyle: 'solid',
              borderWidth: '2px',
              borderColor: '#000',
              borderRadius: '0.25rem',
              backgroundColor: '#fff',
            }}
          >
            {menuItems.map((menuItem) => (
              <NavLink key={menuItem.label} to={menuItem.href}>
                <Button
                  variant="text"
                  color="primary"
                  sx={{
                    padding: '1.25rem',
                    color: `${theme.palette.text.primary}`,
                    fontSize: '0.875rem',
                  }}
                >
                  {menuItem.label}
                </Button>
              </NavLink>
            ))}
          </Box>
        </Toolbar>
      </AppBar>
    </Box>
  );
}

export default NavBar;
