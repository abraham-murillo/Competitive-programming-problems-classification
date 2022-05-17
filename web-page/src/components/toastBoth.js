export function toastBoth(props) {
  const { status, success, failure, toast } = props;

  if (status) {
    toast({
      title: success,
      status: 'success',
      duration: 5000,
      isClosable: true,
    })
  } else {
    toast({
      title: failure,
      status: 'error',
      duration: 5000,
      isClosable: true,
    })
  }
}