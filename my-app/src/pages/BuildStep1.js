import React, { useState } from 'react';
import {
  Box,
  Button,
  TextField
} from '@mui/material';

export default function Build_Itinerary_1() {
  const [resumeContent, setResumeContent] = useState('');
  const [resumeOutput, setResumeOutput] = useState(''); // State for output

  const handleTextAreaChange = (event) => {
    setResumeContent(event.target.value);
  };

  // Simulate a backend call
  const handleGenerateResume = async () => {
    console.log("Sending to backend:", resumeContent);
    
    try {
      const response = await fetch('http://127.0.0.1:5000/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ resumeContent: resumeContent }),
      });
  
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
  
      const data = await response.json();
      setResumeOutput(data.processedContent); // Assuming 'processedContent' is what the backend returns
    } catch (error) {
      console.error('There was a problem with your fetch operation:', error);
    }
  };

  return (
    <div style={{ position: 'relative', height: '100vh', backgroundColor: 'lightyellow', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
      {/* Top Box for displaying the result */}
      <Box
    sx={{
      pt: 2, // Adds padding at the top
      width: '100%',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
    }}
  >
  <TextField
    label="Processed Resume"
    multiline
    rows={4}
    variant="outlined"
    placeholder="Processed resume content will appear here..."
    value={resumeOutput}
    InputProps={{
      readOnly: true, // Makes the text field read-only
    }}
    sx={{
      width: '90%', // Adjust width as per your requirement
      mb: 2,
      backgroundColor: 'white', // Background color
      color: 'black', // Text color
      '& .MuiInputBase-input': {
        color: 'black', // Ensures the text color is black
      },
    }}
  />
</Box>
      {/* Bottom Box for user inputs */}
      <Box
        sx={{
          pb: 10, // Adds padding at the bottom
          width: '100%',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
        }}
      >
        <TextField
          label="Your Resume Inputs"
          multiline
          rows={4}
          variant="outlined"
          placeholder="Insert your resume content here..."
          value={resumeContent}
          onChange={handleTextAreaChange}
          sx={{
            width: '90%', // Adjust width as per your requirement
            mb: 2,
            backgroundColor: 'white', // Background color
            color: 'black', // Text color
          }}
        />
        <Button variant="contained" onClick={handleGenerateResume} sx={{ alignSelf: 'center', bgcolor: 'grey.900' }}>
          Generate your resume
        </Button>
      </Box>
    </div>
  );
}
