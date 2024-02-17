import { useNavigate } from 'react-router-dom';
import backgroundImage from '../static/AstroOrbiter.jpg'; // Import the image from the local path
import { amber } from '@mui/material/colors'
import {Box, Button, Typography} from "@mui/material";
import React from "react";

export default function HomePage() {
  let navigate = useNavigate();

  const BuildStep1 = () => {
    navigate('/buildstep1');
  };

  // Style for the background image container
  const backgroundStyle = {
    backgroundImage: `url(${backgroundImage})`,
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    backgroundRepeat: 'no-repeat',
    filter: 'brightness(70%) grayscale(60%)',
    position: 'absolute', // Position it absolutely to cover the whole container
    top: 0,
    left: 0,
    width: '100%',
    height: '100%',
    zIndex: -1, // Send it to the back
  };

  return (
      <div style={{
        height: '100vh',
        display: 'flex',
        flexDirection: 'column',
      }}>
        {/* Background image container */}
        <div style={backgroundStyle}></div>

        {/* Content container */}
        <Box
          sx={{
            position: 'relative',
            width: '100vw',
            height: '100vh',
            justifyContent:'center',
            alignItems:'center',
          }}
        >
        <Typography
          sx={{
            position: 'absolute',
            top: '48%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            color: '#fff',
            textAlign: 'center',
            zIndex: 1,
          }}
        >
          <Typography
            variant="h2"
            sx={{
              fontFamily: 'Arial',
              fontWeight: 'bold',
              fontSize: { xs: '30pt', sm: '30pt', md: '40pt', lg: '50pt' },
            }}
          >
            One Stop to create your Personal Portfolio
          </Typography>
          <Typography
            variant="body1"
            sx={{
              fontFamily: 'Arial',
              fontSize: { xs: '9pt', sm: '9pt', md: '10pt', lg: '12pt'},
            }}
          >
            Create your professional resume <br/>
            Create your Personal Portfolio Site <br/>
            We've got everything you need to impress the HRs and find your dream job <br/>
          </Typography>

        </Typography>
      </Box>

        <Button sx={{
          position:'absolute',
          alignSelf:'center',
          bottom: '15vh',
          backgroundColor: amber[300],
          textTransform: 'none',
          border: "none",
          borderRadius: '100px',
          boxShadow: '0 4px 8px rgba(0,0,0,0.3)',
          transition: 'all 0.2s ease-in-out',
          height: '60px',
          width: '280px',
          zIndex: 1,
          '&:hover': {
            backgroundColor: amber[200],
          },
          '& .MuiTouchRipple-child': {
          backgroundColor: amber[50],
          },
        }}
          onClick={BuildStep1}
        >
          <Typography
            sx={{
              textAlign:'center',
              fontSize: '18pt',
              fontFamily: 'arial',
              fontWeight: 'bold',
              color: 'white',
            }}
          >
            Get Started
          </Typography>
        </Button>

      </div>
  );
};
