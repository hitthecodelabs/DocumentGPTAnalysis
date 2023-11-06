<template>
  <v-app>
    <v-container fluid>

      <!-- Header -->
      <v-row>
        <v-col class="text-center">
          <h1 class="display-1">PDFs Processing</h1>
          <v-divider></v-divider>
        </v-col>
      </v-row>

      <!-- Welcome Message -->
      <v-row class="mt-5">
        <v-col class="text-center">
          <h2>Welcome to our document upload portal</h2>
          <p>Please upload your documents and answer the questions below.</p>
        </v-col>
      </v-row>

        <!-- Questions & Uploads -->
        <v-row v-for="(question, index) in questions" :key="index" class="mt-5">
            <v-col cols="12" md="8" offset-md="2">
                <v-card>
                    <v-card-title class="headline">Pregunta {{ index }}</v-card-title>
                    <v-card-subtitle>{{ question }}</v-card-subtitle>
                    <v-card-text>
                        <!-- Hidden file input for each question -->
                        <input type="file" :ref="'fileInput' + index" @change="uploadAndProcess(index)" style="display: none;">
                        <!-- Button to trigger file selection -->
                        <v-btn @click="selectFile(index)">Upload File</v-btn>
                        <!-- Display file name if available -->
                        <div v-if="filenames[index]">Uploaded file: {{ filenames[index] }}</div>
                        <!-- Display the answer if available -->
                        <div v-if="answers[index]">
                            <v-divider></v-divider>
                            <strong>Answer:</strong> {{ answers[index] }}
                        </div>
                        <!-- Display loading bar if the question is being processed -->
                        <v-progress-linear v-if="loadingQuestions[index]" indeterminate></v-progress-linear>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>

      <!-- Footer -->
      <v-row class="mt-5">
        <v-col class="text-center">
          <v-divider></v-divider>
          <p>© 2023 Company Name. All rights reserved.</p>
        </v-col>
      </v-row>

    </v-container>
  </v-app>
</template>
