import { red } from '@mui/material/colors';
import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  typography: {
    fontFamily: ['"Martel Sans"', 'sans-serif'].join(','),
  },
  components: {
    MuiButton: {
      root: {
        backgroundColor: '#fff',
      },
    },
  },
  palette: {
    primary: {
      main: '#e48c71',
    },
    secondary: {
      main: '#e48c71',
    },
    error: {
      main: red.A400,
    },
    text: {
      primary: '#222',
    },
    background: {
      default: '#f6efea',
      paper: '#fff',
    },
  },
});

export default theme;
