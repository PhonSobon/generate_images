import os

class TxtFormatter:
    """
    Generates TXT files containing all words rendered in each image
    Preserves the exact layout as it appears in the image with proper spacing
    """
    
    def __init__(self, output_dir="txt_labels"):
        """
        Initialize the TXT formatter
        Args:
            output_dir: Directory where TXT files will be saved
        """
        self.output_dir = output_dir
        
        # Create output directory if it doesn't exist
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            print(f"Created directory: {self.output_dir}/")
    
    def generate_txt_file(self, word_boxes, filename):
        """
        Generate a TXT file with words organized by lines with spaces between words
        Matches the exact readable layout of the document/image
        Args:
            word_boxes: List of dictionaries with word information
            filename: Base filename (without extension)
        """
        txt_path = os.path.join(self.output_dir, f"{filename}.txt")
        
        # Group words by line_id
        lines = {}
        for box in word_boxes:
            line_id = box['line_id']
            if line_id not in lines:
                lines[line_id] = []
            lines[line_id].append(box['text'])
        
        # Write lines in order - words separated by spaces for readability
        with open(txt_path, 'w', encoding='utf-8') as f:
            for line_id in sorted(lines.keys()):
                line_text = " ".join(lines[line_id])  # Space between words
                f.write(line_text + "\n")