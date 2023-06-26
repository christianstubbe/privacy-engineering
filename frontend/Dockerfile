# Dockerfile
# Use an official Node runtime as the base image
FROM node:14

# Set the working directory in the container to /app
WORKDIR /app

# Copy the package.json and package-lock.json files to the new working directory and install the dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of your app's source code to the working directory
COPY . .

# Expose port 3000 for the app to be accessible externally
EXPOSE 3000

# Define the command to run your app using CMD which defines your runtime
# Here we use "npm start" to start your React app
CMD [ "npm", "start" ]
