import React from 'react';
import { Container, Typography, Box } from '@mui/material';

function Home() {
    return (
        <Container>
            <Box
                display="flex"
                flexDirection="column"
                justifyContent="center"
                alignItems="center"
                minHeight="100vh"
                textAlign="center"
            >
                <Typography variant="h2" gutterBottom>
                    Welcome to Our Company
                </Typography>
                <Typography variant="h5">
                    We're committed to providing our customers with the best services.
                </Typography>
                <Box mt={4}>
                    <Typography variant="body1">
                        Our company was founded with a mission to make life better. We're dedicated to providing
                        innovative solutions that improve the quality of life. Our team is passionate about
                        creating products that make a difference. We believe in putting our customers first
                        and are proud of the work we do each day.
                    </Typography>
                </Box>
            </Box>
        </Container>
    );
}

export default Home;
