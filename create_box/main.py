"""This is the entry point of the program."""

def create_box(height, width, character, solid_box=True):
    
    # Test for invalid input.
    if height < 1 or width < 1:
        raise Exception('ArgumentError', 'Height and width must be greater than 0.')
    
    new_string = ""
    
    # Create the box.
    for line in range(height):

        # Test for border box conditions...
        if not solid_box and line > 0 and line < (height - 1) and width > 2:
            new_string += character + ' '*(width-2) + character + '\n'
            
        # Add a normal line.
        else:
            new_string += (character*width + '\n')

    # Send the line back!    
    return new_string


if __name__ == '__main__':
    create_box(3, 4, '*')
    create_box(25, 105, '&', False)
#    create_box(0, 0, '*')