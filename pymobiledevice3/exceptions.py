__all__ = [
    'PyMobileDevice3Exception', 'DeviceVersionNotSupportedError', 'IncorrectModeError',
    'NotTrustedError', 'PairingError', 'NotPairedError', 'CannotStopSessionError',
    'PasswordRequiredError', 'StartServiceError', 'FatalPairingError', 'NoDeviceConnectedError', 'DeviceNotFoundError',
    'TunneldConnectionError', 'ConnectionFailedToUsbmuxdError', 'MuxException', 'InvalidConnectionError',
    'MuxVersionError', 'ArgumentError', 'AfcException', 'AfcFileNotFoundError', 'DvtException', 'DvtDirListError',
    'NotMountedError', 'AlreadyMountedError', 'UnsupportedCommandError', 'ExtractingStackshotError',
    'ConnectionTerminatedError', 'WirError', 'WebInspectorNotEnabledError', 'RemoteAutomationNotEnabledError',
    'ArbitrationError', 'InternalError', 'DeveloperModeIsNotEnabledError', 'DeviceAlreadyInUseError', 'LockdownError',
    'PairingDialogResponsePendingError', 'UserDeniedPairingError', 'InvalidHostIDError', 'SetProhibitedError',
    'MissingValueError', 'PasscodeRequiredError', 'AmfiError', 'DeviceHasPasscodeSetError', 'NotificationTimeoutError',
    'DeveloperModeError', 'ProfileError', 'IRecvError', 'IRecvNoDeviceConnectedError', 'UnrecognizedSelectorError',
    'MessageNotSupportedError', 'InvalidServiceError', 'InspectorEvaluateError',
    'LaunchingApplicationError', 'BadCommandError', 'BadDevError', 'ConnectionFailedError', 'CoreDeviceError',
    'AccessDeniedError', 'RSDRequiredError', 'SysdiagnoseTimeoutError', 'GetProhibitedError',
    'FeatureNotSupportedError', 'OSNotSupportedError', 'DeprecationError', 'NotEnoughDiskSpaceError',
    'CloudConfigurationAlreadyPresentError', 'QuicProtocolNotSupportedError', 'RemotePairingCompletedError',
    'DisableMemoryLimitError',
]

from typing import Optional


class PyMobileDevice3Exception(Exception):
    pass


class DeviceVersionNotSupportedError(PyMobileDevice3Exception):
    pass


class IncorrectModeError(PyMobileDevice3Exception):
    pass


class NotTrustedError(PyMobileDevice3Exception):
    pass


class PairingError(PyMobileDevice3Exception):
    pass


class NotPairedError(PyMobileDevice3Exception):
    pass


class CannotStopSessionError(PyMobileDevice3Exception):
    pass


class PasswordRequiredError(PairingError):
    pass


class StartServiceError(PyMobileDevice3Exception):
    pass


class FatalPairingError(PyMobileDevice3Exception):
    pass


class NoDeviceConnectedError(PyMobileDevice3Exception):
    pass


class InterfaceIndexNotFoundError(PyMobileDevice3Exception):
    def __init__(self, address: str):
        super().__init__()
        self.address = address


class DeviceNotFoundError(PyMobileDevice3Exception):
    def __init__(self, udid: str):
        super().__init__()
        self.udid = udid


class TunneldConnectionError(PyMobileDevice3Exception):
    pass


class MuxException(PyMobileDevice3Exception):
    pass


class MuxVersionError(MuxException):
    pass


class BadCommandError(MuxException):
    pass


class BadDevError(MuxException):
    pass


class ConnectionFailedError(MuxException):
    pass


class ConnectionFailedToUsbmuxdError(ConnectionFailedError):
    pass


class ArgumentError(PyMobileDevice3Exception):
    pass


class AfcException(PyMobileDevice3Exception, OSError):
    def __init__(self, message, status):
        OSError.__init__(self, status, message)
        self.status = status


class AfcFileNotFoundError(AfcException):
    pass


class DvtException(PyMobileDevice3Exception):
    """ Domain exception for DVT operations. """
    pass


class UnrecognizedSelectorError(DvtException):
    """ Attempted to call an unrecognized selector from DVT. """
    pass


class DvtDirListError(DvtException):
    """ Raise when directory listing fails. """
    pass


class NotMountedError(PyMobileDevice3Exception):
    """ Given image for umount wasn't mounted in the first place """
    pass


class AlreadyMountedError(PyMobileDevice3Exception):
    """ Given image for mount has already been mounted in the first place """
    pass


class MissingManifestError(PyMobileDevice3Exception):
    """ No manifest could be found """
    pass


class UnsupportedCommandError(PyMobileDevice3Exception):
    """ Given command isn't supported for this iOS version """
    pass


class ExtractingStackshotError(PyMobileDevice3Exception):
    """ Raise when stackshot is not received in the core profile session. """
    pass


class ConnectionTerminatedError(PyMobileDevice3Exception):
    """ Raise when a connection is terminated abruptly. """
    pass


class StreamClosedError(ConnectionTerminatedError):
    """ Raise when trying to send a message on a closed stream. """
    pass


class WebInspectorNotEnabledError(PyMobileDevice3Exception):
    """ Raise when Web Inspector is not enabled. """
    pass


class RemoteAutomationNotEnabledError(PyMobileDevice3Exception):
    """ Raise when Web Inspector remote automation is not enabled. """
    pass


class WirError(PyMobileDevice3Exception):
    """ Raise when Webinspector WIR command fails. """
    pass


class InternalError(PyMobileDevice3Exception):
    """ Some internal Apple error """
    pass


class ArbitrationError(PyMobileDevice3Exception):
    """ Arbitration failed """
    pass


class DeviceAlreadyInUseError(ArbitrationError):
    """ Device is already checked-in by someone """

    @property
    def message(self):
        return self.args[0].get('message')

    @property
    def owner(self):
        return self.args[0].get('owner')

    @property
    def result(self):
        return self.args[0].get('result')


class DeveloperModeIsNotEnabledError(PyMobileDevice3Exception):
    """ Raise when mounting failed because developer mode is not enabled. """
    pass


class DeveloperDiskImageNotFoundError(PyMobileDevice3Exception):
    """ Failed to locate the correct DeveloperDiskImage.dmg """
    pass


class DeveloperModeError(PyMobileDevice3Exception):
    """ Raise when amfid failed to enable developer mode. """
    pass


class LockdownError(PyMobileDevice3Exception):
    """ lockdown general error """

    def __init__(self, message: str, identifier: Optional[str] = None) -> None:
        super().__init__(message)
        self.identifier = identifier


class GetProhibitedError(LockdownError):
    pass


class SetProhibitedError(LockdownError):
    pass


class PairingDialogResponsePendingError(PairingError):
    """ User hasn't yet confirmed the device is trusted """
    pass


class UserDeniedPairingError(PairingError):
    pass


class InvalidHostIDError(PairingError):
    pass


class MissingValueError(LockdownError):
    """ raised when attempting to query non-existent domain/key """
    pass


class InvalidConnectionError(LockdownError):
    pass


class PasscodeRequiredError(LockdownError):
    """ passcode must be present for this action """
    pass


class AmfiError(PyMobileDevice3Exception):
    pass


class DeviceHasPasscodeSetError(AmfiError):
    pass


class NotificationTimeoutError(PyMobileDevice3Exception, TimeoutError):
    pass


class ProfileError(PyMobileDevice3Exception):
    pass


class CloudConfigurationAlreadyPresentError(ProfileError):
    pass


class IRecvError(PyMobileDevice3Exception):
    pass


class IRecvNoDeviceConnectedError(IRecvError):
    pass


class MessageNotSupportedError(PyMobileDevice3Exception):
    pass


class InvalidServiceError(LockdownError):
    pass


class InspectorEvaluateError(PyMobileDevice3Exception):
    def __init__(self, class_name: str, message: str, line: Optional[int] = None, column: Optional[int] = None,
                 stack: Optional[list[str]] = None):
        super().__init__()
        self.class_name = class_name
        self.message = message
        self.line = line
        self.column = column
        self.stack = stack

    def __str__(self) -> str:
        stack_trace = '\n'.join([f'\t - {frame}' for frame in self.stack])
        return (f'{self.class_name}: {self.message}.\n'
                f'Line: {self.line} Column: {self.column}\n'
                f'Stack: {stack_trace}')


class LaunchingApplicationError(PyMobileDevice3Exception):
    pass


class AppInstallError(PyMobileDevice3Exception):
    pass


class AppNotInstalledError(PyMobileDevice3Exception):
    pass


class CoreDeviceError(PyMobileDevice3Exception):
    pass


class AccessDeniedError(PyMobileDevice3Exception):
    """ Need extra permissions to execute this command """
    pass


class NoSuchBuildIdentityError(PyMobileDevice3Exception):
    pass


class MobileActivationException(PyMobileDevice3Exception):
    """ Mobile activation can not be done """
    pass


class NotEnoughDiskSpaceError(PyMobileDevice3Exception):
    """ Computer does not have enough disk space for the intended operation """
    pass


class DeprecationError(PyMobileDevice3Exception):
    """ The requested action/service/method is deprecated """
    pass


class RSDRequiredError(PyMobileDevice3Exception):
    """ The requested action requires an RSD object """

    def __init__(self, identifier: str) -> None:
        self.identifier = identifier
        super().__init__()


class SysdiagnoseTimeoutError(PyMobileDevice3Exception, TimeoutError):
    """ Timeout collecting new sysdiagnose archive """
    pass


class SupportError(PyMobileDevice3Exception):
    def __init__(self, os_name):
        self.os_name = os_name
        super().__init__()


class OSNotSupportedError(SupportError):
    """ Operating system is not supported. """
    pass


class FeatureNotSupportedError(SupportError):
    """ Feature has not been implemented for OS. """

    def __init__(self, os_name, feature):
        super().__init__(os_name)
        self.feature = feature


class QuicProtocolNotSupportedError(PyMobileDevice3Exception):
    """ QUIC tunnel support was removed on iOS 18.2+ """
    pass


class RemotePairingCompletedError(PyMobileDevice3Exception):
    """
    Raised upon pairing completion using the `remotepairingdeviced` service (RemoteXPC).

    remotepairingdeviced closes connection after pairing, so client must re-establish it after pairing is
    completed.
    """
    pass


class DisableMemoryLimitError(PyMobileDevice3Exception):
    """ Disabling memory limit fails. """
    pass


class ProtocolError(PyMobileDevice3Exception):
    """ An unexpected protocol message was received """
    pass
