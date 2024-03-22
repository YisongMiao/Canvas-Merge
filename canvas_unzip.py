import os
import regex as re


def unzip_files():
    assignment_dir = 'a2-submissions'
    # Loop through all zip files in the assignment directory

    number_of_zip_file = 0
    for zip_file in os.listdir(assignment_dir):
        # check if the file is a zip file
        if not zip_file.endswith('.zip'):
            continue
        # # print the name of the zip file
        # print(zip_file)
        number_of_zip_file += 1

        # # extract the student number in the format of A[0-9]+[A-Z]
        student_number = re.search(r'A[0-9]+[A-Z]', zip_file)

        # # print the student number
        try: 
            # print(student_number.group())
            student_number = student_number.group()
        except AttributeError:
            print('No student number found')
            # This is actually no submission file, but some attachment (e.g. model). 
            print(zip_file)
            continue
        
        # Output dir is called "a2-clean"
        output_dir = 'a2-clean'
        # Create the output directory if it does not exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        # Create the student directory if it does not exist
        student_dir = os.path.join(output_dir, student_number)
        if not os.path.exists(student_dir):
            os.makedirs(student_dir)
        # Unzip the file into the student directory, we want to make an a condition that, if a file is larger than 50MB, we will not unzip it
        if os.path.getsize(os.path.join(assignment_dir, zip_file)) < 50 * 1024 * 1024:
            os.system(f'unzip -o {os.path.join(assignment_dir, zip_file)} -d {student_dir}')
        else:
            print(f'The file {zip_file} is too large to unzip')
    print(f'Number of zip files: {number_of_zip_file}')


def clean():
    # Go through all the student directories in a recursive manner, and remove all files that is bigger than 50MB
    for root, dirs, files in os.walk('a2-clean'):
        for file in files:
            if os.path.getsize(os.path.join(root, file)) > 50 * 1024 * 1024:
                print(f'Removing file {os.path.join(root, file)}')
                os.remove(os.path.join(root, file))


if __name__ == '__main__':
    # unzip_files()
    clean()

