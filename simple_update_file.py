import re

def simple_update_file(dic, \
                       name='inlist_project', \
                       comment_character='!'):
    '''
    
    Purpose:
        
        Update valueas in a text file
        

    Description:   
        
        The default layout of the value to update is: 
            
            key = value ! Comment
            
        Note that white spaces are permitted at any position within the line.
        
        The comment character can be redefined with comment_character.
        
        key and value cannot contain spaces
        
             
    Call:
        
        dic={str:str,str:str}
        simple_update_file(dic, name='inlist_project')
        
        
    Parameters:
        
        dic -   Dictionary containing the name of the parameter to update 
                and the new value. E.g. dic={'initial_mass:'1.0'}
        
        name -  Path of the file to be updated. E.g.:
                name = '\path\to\file.txt'
                
        comment_character -     Character to the right of this character will 
                                be ignored/skipped.

    Example:

        dic={'initial_mass:'1.0',
             'profile_columns_file':"'extra_profile_columns'"}
        simple_update_file(dic, \
                           name='inlist_project', \
                           comment_character='!')
        
    To improve:
        
        
    '''

    # Open file
    f = open(name)
    # Read all lines
    lines = f.readlines()
    nlines = len(lines)
    # Close file
    f.close()

    # Iteration for the values we want to update
    for key, value in dic.items():
        
        #Iteration over the lines
        for iline, line in enumerate(lines):
            
            # We skip comment lines
            if not re.match(r'^ *'+comment_character,line):
                # We check if there is still a comment character in the line
                comment = re.search(comment_character,line)
                
                if comment:
                    # We split the line by the comment character
                    splits = line.split(comment_character)      
                    no_comment = splits[0]                
                    # We check for the key
                    match = re.match(r'(\s*)('+key+')(\s*)(=)(\s*)(\S*)(\s*)',no_comment)
                
                    if match:
                        # Get tuple with the groups and make a list
                        new_line_list = [i for i in match.groups()]
                        # Update the value
                        new_line_list[5] = value
                        # Convert list to string
                        new_line_str = ''
                        new_line_str = new_line_str.join(new_line_list)
                        
                        # Update the value
                        splits[0] = new_line_str
                        lines[iline] = comment_character.join(splits)
                        break
                    
                else:
                    no_comment = line                
                    # We check for the key
                    match = re.match(r'(\s*)('+key+')(\s*)(=)(\s*)(\S*)(\s*)',no_comment)
                
                    if match:
                        # Get tuple with the groups and make a list
                        new_line_list = [i for i in match.groups()]
                        # Update the value
                        new_line_list[5] = value
                        # Convert list to string
                        new_line_str = ''
                        new_line_str = new_line_str.join(new_line_list)
                        
                        # Update the value
                        lines[iline] = new_line_str
                        break
                                     
    f = open(name,'w')
    f.writelines(lines)
    f.close()
