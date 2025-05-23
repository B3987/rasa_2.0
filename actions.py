from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionHandleButtonClick(Action):
    def name(self) -> Text:
        return "action_handle_button_click"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        intent = tracker.latest_message['intent'].get('name')
        
        # 1. First send the original message from domain.yml
        dispatcher.utter_message(response=f"utter_{intent}")
        
        # 2. Then send the JSON payload
        payload = self._get_payload_for_intent(intent)
        if payload:
            dispatcher.utter_message(json_message=payload)
        
        return []
    
    def _get_payload_for_intent(self, intent: Text) -> Dict[Text, Any]:
        """Returns the complete payload mapping for all intents"""
        payload_map = {
            # ========== ESS Intents ==========
            "ess_apply_leave": {
                "Message": "ESS",
                "URL": "/ess/my-leave",
                "Authorities": ["ROLE_EMPLOYEE"]
            },
            "ess_cancel_leave": {
                "Message": "ESS",
                "URL": "/ess/leave-cancel",
                "Authorities": ["ROLE_EMPLOYEE"]
            },
            "ess_revoke_leave": {
                "Message": "ESS",
                "URL": "/ess/leave-revoke",
                "Authorities": ["ROLE_EMPLOYEE"]
            },
            "ess_mark_attendance": {
                "Message": "ESS",
                "URL": "/ess/mark-attendance",
                "Authorities": ["ROLE_EMPLOYEE"]
            },
            "ess_request_attendance_correction": {
                "Message": "ESS",
                "URL": "/ess/attendance-correction",
                "Authorities": ["ROLE_EMPLOYEE"]
            },
            
            # ========== Manager Intents ==========
            "manager_approve_leave": {
                "Message": "MANAGER",
                "URL": "/manager/approve-leave",
                "Authorities": ["ROLE_MANAGER"]
            },
            
            # ========== Payroll Intents ==========
            "payroll_request": {
                "Message": "PAYROLL",
                "URL": "/payroll/request",
                "Authorities": ["ROLE_ADMIN"]
            },
            "payroll_run": {
                "Message": "PAYROLL",
                "URL": "/payroll/run",
                "Authorities": ["ROLE_ADMIN"]
            },
            "payroll_add_employee": {
                "Message": "PAYROLL",
                "URL": "/payroll/add-employee",
                "Authorities": ["ROLE_ADMIN"]
            },
            
            # ========== Employee Management Intents ==========
            "emp_mgmt_create": {
                "Message": "EMPLOYEE_MGMT",
                "URL": "/admin/employee/create",
                "Authorities": ["ROLE_ADMIN"]
            },
            "emp_mgmt_update": {
                "Message": "EMPLOYEE_MGMT",
                "URL": "/admin/employee/update",
                "Authorities": ["ROLE_ADMIN"]
            },
            
            # ========== Organization Setup Intents ==========
            "org_update_branch": {
                "Message": "ORG_SETUP",
                "URL": "/admin/organization/branch",
                "Authorities": ["ROLE_ADMIN"]
            },
            "org_update_department": {
                "Message": "ORG_SETUP",
                "URL": "/admin/organization/department",
                "Authorities": ["ROLE_ADMIN"]
            },
            "org_update_working_days": {
                "Message": "ORG_SETUP",
                "URL": "/admin/organization/working-days",
                "Authorities": ["ROLE_ADMIN"]
            },
            "org_update_attendance_location": {
                "Message": "ORG_SETUP",
                "URL": "/admin/organization/attendance-location",
                "Authorities": ["ROLE_ADMIN"]
            },
            
            # ========== Company Settings Intents ==========
            "company_update_details": {
                "Message": "COMPANY_SETTINGS",
                "URL": "/admin/company/details",
                "Authorities": ["ROLE_ADMIN"]
            },
            "company_update_leave_types": {
                "Message": "COMPANY_SETTINGS",
                "URL": "/admin/company/leave-types",
                "Authorities": ["ROLE_ADMIN"]
            },
            "company_update_terms": {
                "Message": "COMPANY_SETTINGS",
                "URL": "/admin/company/terms",
                "Authorities": ["ROLE_ADMIN"]
            },
            
            # ========== System Intents ==========
            "greet": {
                "Message": "SYSTEM",
                "URL": None,
                "Authorities": []
            },
            "thank": {
                "Message": "SYSTEM",
                "URL": None,
                "Authorities": []
            },
            "goodbye": {
                "Message": "SYSTEM",
                "URL": None,
                "Authorities": []
            }
        }
        
        return payload_map.get(intent)

# Note: The above code assumes that the payloads are static and predefined.