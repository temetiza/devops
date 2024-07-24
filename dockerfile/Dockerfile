# FROM node:14

# WORKDIR /usr/src/app

# COPY package*.json ./
# RUN npm install

# COPY . .

# EXPOSE 3000
# CMD [ "node", "app.js" ]
# FROM python:3

# WORKDIR /app

# COPY requirements.txt /app
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# EXPOSE 5000
# CMD [ "python", "app.py" ]


# Use an official Node.js runtime as the base image
FROM node:14

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the application code to the working directory
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Command to run the application
CMD ["node", "app.js"]
