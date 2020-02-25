/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.flink.statefun.itcases.sanity;

import static org.apache.flink.statefun.itcases.sanity.Constants.FUNCTION_TYPES;

import org.apache.flink.statefun.itcases.sanity.generated.VerificationMessages;
import org.apache.flink.statefun.sdk.Address;
import org.apache.flink.statefun.sdk.FunctionType;

final class Utils {

  private Utils() {}

  static Address toSdkAddress(VerificationMessages.FnAddress target) {
    FunctionType targetType = FUNCTION_TYPES[target.getType()];
    return new Address(targetType, target.getId());
  }
}