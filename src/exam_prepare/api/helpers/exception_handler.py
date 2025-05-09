from __future__ import annotations

from enum import Enum
from typing import Optional

from fastapi import status
from fastapi.responses import JSONResponse
from shared.base import BaseModel
from structlog.stdlib import BoundLogger


class ResponseMessage(str, Enum):
    INTERNAL_SERVER_ERROR = "Server might meet some errors. \
    Please try again later !!!"
    SUCCESS = "Process successfully !!!"
    NOT_FOUND = "Resource not found !!!"
    BAD_REQUEST = "Invalid request !!!"
    UNPROCESSABLE_ENTITY = "Input is not allowed !!!"
    INVALID_API_KEY = "Invalid API key !!!"


class ExceptionHandler(BaseModel):
    logger: BoundLogger
    service_name: str

    @staticmethod
    def create_response_message(message):
        """Create a response message
        Args:
            message (str): message to be returned
        Returns:
            dict: response message
        """
        response_data = {"message": message}
        return response_data

    def _create_message(self, e: str) -> str:
        return f"[{self.service_name}] error: {e}"

    def _create_response(
        self,
        message: str,
        data: Optional[dict] = None,
        status_code: int = status.HTTP_200_OK,
    ) -> JSONResponse:
        """Create a response object
        Args:
            message (str): message to be returned
            data (Optional[dict], optional): data to be returned.
            Defaults to None.
            status_code (int, optional): status code of the response.
            Defaults to status.HTTP_200_OK.
        Returns:
            Response: response object
        """
        response_data = self.create_response_message(message)
        if data:
            response_data.update(data)
        return JSONResponse(content=response_data, status_code=status_code)

    def handle_exception(self, message: str, extra: dict) -> JSONResponse:
        """Handle exception
        Args:
            e (str): exception message
            extra (dict): extra information
        Returns:
            Response: response object
        """
        self.logger.exception(message, extra=extra)
        return self._create_response(
            ResponseMessage.INTERNAL_SERVER_ERROR.value,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    def handle_not_found_error(self, message: str, extra: dict) -> JSONResponse:
        """Handle not found error
        Args:
            message (str): message
            extra (dict): extra information
        Returns:
            Response: response object
        """
        self.logger.error(
            message,
            extra=extra,
        )
        return self._create_response(
            ResponseMessage.NOT_FOUND.value,
            status_code=status.HTTP_404_NOT_FOUND,
        )

    def handle_success(self, output: dict) -> JSONResponse:
        """Handle success
        Args:
            output (dict): output
        Returns:
            Response: response object
        """
        data = {"info": output}
        return self._create_response(
            ResponseMessage.SUCCESS.value,
            data=data,
            status_code=status.HTTP_200_OK,
        )

    def handle_bad_request(self, message: str, extra: dict) -> JSONResponse:
        """Handle bad request
        Args:
            message (str): message
            extra (dict): extra information
        Returns:
            Response: response object
        """
        self.logger.error(
            message,
            extra=extra,
        )
        return self._create_response(
            ResponseMessage.BAD_REQUEST.value,
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    # type: ignore
    # type: ignore
    def handle_unprocessable_entity(self, message: str, extra: dict) -> JSONResponse:
        self.logger.error(
            message,
            extra=extra,
        )
        return self._create_response(
            ResponseMessage.UNPROCESSABLE_ENTITY.value,
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        )
