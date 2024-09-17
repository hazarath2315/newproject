def log_function(func):
  def wrapper(*args, **kwargs):
    #print(f"Function {func.name} called with arguments {args} and keyword arguments {kwargs}")
    result = func(*args, **kwargs)
    
    return result
  return wrapper

def authentication(func):
  def wrapper(*args, **kwargs):
    # Authentication logic here
    
      return func(*args, **kwargs)
    
  return wrapper

@log_function  # This is applied first
@authentication  # This is applied second
def do_something(name):
  return f"Doing something for {name}"
  return f"Result for {name}"

print(do_something("Alice"))