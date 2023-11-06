export default {
  data() {
    return {
      uploadResponse: '',
      documentList: [],
      answers: {},
      questions: {},
      loadingQuestions: {},  // Object to track which questions are being processed
      filenames: {}
    };
  },
  mounted() {
    // Fetch the questions when the component is mounted
    fetch('http://localhost:5000/questions')
    .then(response => response.json())
    .then(data => {
        console.log(data);  // Log the fetched questions
        this.questions = data;
    })
    .catch(error => {
        console.error("There was an error fetching the questions:", error);
    });
  },
  methods: {
    selectFile(questionNumber) {
        let refName;
        if (questionNumber === 'document') {
            refName = 'documentInput';
        } else {
            refName = 'fileInput' + questionNumber;
        }
    
        console.log('Ref:', this.$refs[refName]);
    
        const inputFile = this.$refs[refName];
        if (Array.isArray(inputFile)) {
            inputFile[0].click();  // If it's an array, use the first element
        } else {
            inputFile.click();  // If it's a single DOM element, just call the click method
        }
    },    
    async uploadFile(event, type) {
        const file = event.target.files[0];
        if (!file) return;
      
        const formData = new FormData();
        formData.append('file', file);
        
        try {
          let endpoint = 'http://localhost:5000/upload';
          if (type === 'answer') {
            endpoint += `/answer/${file.name}`;
          }
      
          const response = await fetch(endpoint, {
            method: 'POST',
            body: formData
          });
          const data = await response.json();
          this.uploadResponse = data.result;
      
          // If the file is uploaded from the document section
          if (type === 'document') {
            this.documentList = [];  // clear the list after upload
          }
        } catch (error) {
          console.error("There was an error uploading the file:", error);
        }
    },
    async uploadDocuments() {
        for (const doc of this.documentList) {
          const formData = new FormData();
          formData.append('file', doc);
          await this.uploadFile({ target: { files: [doc] } }, 'document');
        }
      
        // After all documents are uploaded, request the backend to process them
        try {
          const response = await fetch('http://localhost:5000/process_files', {
            method: 'POST'
          });
          const data = await response.json();
          this.answers = data;  // Store the answers
        } catch (error) {
          console.error("There was an error processing the files:", error);
        }
    },
    addToDocumentList(event) {
        const files = Array.from(event.target.files);
        this.documentList.push(...files);
    },
    async uploadAndProcess(questionNumber) {
        const file = event.target.files[0];
        if (!file) return;
          
        const formData = new FormData();
        formData.append('file', file);

        // Now initiate the file upload and processing
        this.filenames[questionNumber] = file.name;
    
        this.loadingQuestions[questionNumber] = true;  // Set the question to loading state
    
        try {
            const response = await fetch('http://localhost:5000/upload/' + questionNumber, {
                method: 'POST',
                body: formData
            });
            const data = await response.json();
            this.answers[questionNumber] = data.result;
        } catch (error) {
            console.error("There was an error processing the file:", error);
        } finally {
            this.loadingQuestions[questionNumber] = false;  // Set the question to not loading state
        }
    },
  }
}