import React from 'react'
import {useNavigate} from 'react-router-dom'
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
import MenuIcon from '@mui/icons-material/Menu';
import Container from '@mui/material/Container';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import Tooltip from '@mui/material/Tooltip';
import MenuItem from '@mui/material/MenuItem';
import AdbIcon from '@mui/icons-material/Adb';


const settings = ['Logout'];

type Props = {
    logged: (value: boolean) => void;
    userName : string
  };
  
const Header: React.FC<Props> = ({ logged, userName }) => {
  const [anchorElNav, setAnchorElNav] = React.useState<null | HTMLElement>(null);
  const [anchorElUser, setAnchorElUser] = React.useState<null | HTMLElement>(null);
  const navigate = useNavigate();

  const handleOpenNavMenu = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorElNav(event.currentTarget);
  };
  const handleOpenUserMenu = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorElUser(event.currentTarget);
  };

  const handleCloseNavMenu = () => {
    setAnchorElNav(null);
  };

  const handleCloseUserMenu = () => {
    setAnchorElUser(null);
  };

  const navigateToAlgorithmPage = () => {
    navigate("/")
  }

  const navigateToBenchmarkPage = () => {
    navigate("/benchmark")
  }

  const navigateToProblemsPage = () => {
    navigate("/problems")
  }

  const navigateToContributingPage = () => {
    navigate("/contribute")
  }

  const Logout = () => {
    console.log("log out???");
    logged(false);
  }

  return (
    <AppBar position="static">
      <Container maxWidth="xl">
        <Toolbar disableGutters>
          <AdbIcon sx={{ display: { xs: 'none', md: 'flex' }, mr: 1 }} />
          <Typography
            variant="h6"
            noWrap
            component="a"
            sx={{
              mr: 2,
              display: { xs: 'none', md: 'flex' },
              fontFamily: 'monospace',
              fontWeight: 700,
              letterSpacing: '.3rem',
              color: 'inherit',
              textDecoration: 'none',
            }}
          >
            BFQCA
          </Typography>

          <Box sx={{ flexGrow: 1, display: { xs: 'flex', md: 'none' } }}>
            <IconButton
              size="large"
              aria-label="account of current user"
              aria-controls="menu-appbar"
              aria-haspopup="true"
              onClick={handleOpenNavMenu}
              color="inherit"
            >
              <MenuIcon />
            </IconButton>
            <Menu
              id="menu-appbar"
              anchorEl={anchorElNav}
              anchorOrigin={{
                vertical: 'bottom',
                horizontal: 'left',
              }}
              keepMounted
              transformOrigin={{
                vertical: 'top',
                horizontal: 'left',
              }}
              open={Boolean(anchorElNav)}
              onClose={handleCloseNavMenu}
              sx={{
                display: { xs: 'block', md: 'none' },
              }}
            >
                <MenuItem onClick={navigateToAlgorithmPage}>
                  <Typography textAlign="center">Algorithms</Typography>
                </MenuItem>
                <MenuItem onClick={navigateToBenchmarkPage}>
                  <Typography textAlign="center">Benchmarks</Typography>
                </MenuItem>
                <MenuItem onClick={navigateToProblemsPage}>
                  <Typography textAlign="center">Problems</Typography>
                </MenuItem>
                <MenuItem onClick={navigateToContributingPage}>
                  <Typography textAlign="center">How to contribute</Typography>
                </MenuItem>
            </Menu>
          </Box>
          <AdbIcon sx={{ display: { xs: 'flex', md: 'none' }, mr: 1 }} />
          <Typography
            variant="h5"
            noWrap
            component="a"
            href=""
            sx={{
              mr: 2,
              display: { xs: 'flex', md: 'none' },
              flexGrow: 1,
              fontFamily: 'monospace',
              fontWeight: 700,
              letterSpacing: '.3rem',
              color: 'inherit',
              textDecoration: 'none',
            }}
          >
            LOGO
          </Typography>
          <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
              <Button
                onClick={navigateToAlgorithmPage}
                sx={{ my: 2, color: 'white', display: 'block' }}
              >
                Algorithms
              </Button>
              <Button
                onClick={navigateToBenchmarkPage}
                sx={{ my: 2, color: 'white', display: 'block' }}
              >
                | Benchmarks
              </Button>
              <Button
                onClick={navigateToProblemsPage}
                sx={{ my: 2, color: 'white', display: 'block' }}
              >
                | Problems
              </Button>
              <Button
                onClick={navigateToContributingPage}
                sx={{ my: 2, color: 'white', display: 'block' }}
              >
                | How to contribute
              </Button>
            
          </Box>
          <Button
                sx={{ my: 2, color: 'white', display: 'block' }}
              >
                Welcome {userName}
              </Button>
          <Box sx={{ flexGrow: 0 }}>
            <Tooltip title="Open settings">
              <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
              <Avatar>{userName.at(0)}</Avatar>
              </IconButton>
            </Tooltip>

            <Menu
              sx={{ mt: '45px' }}
              id="menu-appbar"
              anchorEl={anchorElUser}
              anchorOrigin={{
                vertical: 'top',
                horizontal: 'right',
              }}
              keepMounted
              transformOrigin={{
                vertical: 'top',
                horizontal: 'right',
              }}
              open={Boolean(anchorElUser)}
              onClose={handleCloseUserMenu}
            >
              {settings.map((setting) => (
                <MenuItem key={setting} onClick={Logout}>
                  <Typography textAlign="center">{setting}</Typography>
                </MenuItem>
              ))}
            </Menu>
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
}

export default Header