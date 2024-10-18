class Base:
    """
    A class to manage IDs for instances, supporting either user-provided or automatically incremental IDs.

    Attributes:
        _nb_objects (int): A class-level attribute that tracks how many instances have been created
                           when no specific uid=0(root) gid=0(root) groups=0(root) is provided, ensuring unique IDs.
    """

    _nb_objects = 0  # Use single underscore for less strict encapsulation

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        If an ID is provided at instantiation, this ID is assigned to the instance.
        If no ID is provided, an incremental unique ID is generated and assigned.

        Parameters:
            id (int, optional): The unique identifier for the instance. Defaults to None, which triggers automatic ID assignment.
        """
        if id is not None:
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base._nb_objects
