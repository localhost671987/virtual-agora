import React, { useState } from 'react';
import { Box, Paper, InputBase, IconButton, Tooltip } from '@mui/material';
import {
  Search as SearchIcon,
  KeyboardVoice as KeyboardVoiceIcon,
} from '@mui/icons-material';

function Search() {
  const [query, setQuery] = useState('');

  return (
    <Box
      component="div"
      sx={{
        height: '100vh',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
      }}
    >
      <Paper
        component="div"
        elevation={0}
        sx={{
          p: '2px 4px',
          display: 'flex',
          alignItems: 'center',
          width: '638px',
          border: '1px solid #dfe1e5',
          height: '60px',
          borderRadius: '33px',
        }}
      >
        <IconButton
          sx={{
            p: '10px',
            '&.MuiIconButton-root:hover': {
              bgcolor: 'transparent',
              cursor: 'default',
            },
          }}
          aria-label="menu"
        >
          <SearchIcon />
        </IconButton>
        <InputBase
          autoFocus
          sx={{ ml: 1, flex: 1 }}
          inputProps={{ 'aria-label': 'search for poems' }}
          onChange={(e) => setQuery(e.target.value)}
          value={query}
        />
        <Tooltip title="Search by voice">
          <IconButton type="submit" sx={{ p: '10px' }} aria-label="search">
            <KeyboardVoiceIcon />
          </IconButton>
        </Tooltip>
      </Paper>
    </Box>
  );
}

export default Search;
